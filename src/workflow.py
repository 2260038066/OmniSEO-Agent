from src.agents.scraper import ScraperAgent
from src.agents.generator import GeneratorAgent
from src.agents.critic import CriticAgent
from src.utils.logger import logger

class OmniSEOWorkflow:
    def __init__(self, config):
        self.config = config
        self.scraper = ScraperAgent()
        self.generator = GeneratorAgent(config['brand_settings'], config['seo_targets'])
        self.critic = CriticAgent(config['seo_targets'])
        self.max_retries = config['project']['max_retries']
        self.pass_score = config['project']['pass_score']
        self.languages = config['languages']

    def run(self, task):
        # 步骤 1: 抓取竞品提取卖点
        selling_points = self.scraper.extract_features(task['competitor_urls'])
        logger.info(f"提炼卖点完成: {selling_points}")

        final_contents = {}

        # 步骤 2: 多语言循环处理
        for lang in self.languages:
            logger.info(f"=== 开始生成语言: {lang} ===")
            content = ""
            critic_feedback = "初始生成"
            
            # 步骤 3: Actor-Critic 重写闭环 (核心消耗 Token 的地方)
            for attempt in range(self.max_retries):
                logger.info(f"[{lang}] 第 {attempt + 1} 次尝试生成...")
                
                # Generator 生成内容
                content = self.generator.generate(selling_points, lang, critic_feedback)
                
                # Critic 评估内容
                score, feedback = self.critic.evaluate(content, lang)
                logger.info(f"[{lang}] Critic 评分: {score}/100. 反馈: {feedback}")

                if score >= self.pass_score:
                    logger.info(f"[{lang}] ✅ 质量达标，进入发布队列。")
                    final_contents[lang] = content
                    break
                else:
                    critic_feedback = feedback
                    logger.warning(f"[{lang}] ⚠️ 质量未达标，将根据反馈进行重写...")
            
            if lang not in final_contents:
                logger.error(f"[{lang}] 达到最大重试次数，任务中止。")
                return None

        return final_contents