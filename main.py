import yaml
import os
from dotenv import load_dotenv
from src.workflow import OmniSEOWorkflow
from src.utils.logger import logger

def main():
    # 1. 加载配置项
    load_dotenv()
    if not os.getenv("LLM_API_KEY"):
        logger.error("未找到 LLM_API_KEY，请检查 .env 文件。")
        return

    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    logger.info("OmniSEO 引擎启动，读取配置成功。")

    # 2. 模拟从 input.csv 读取的任务数据
    # 实际生产环境中这里将遍历 CSV 或数据库
    mock_task = {
        "sku_id": "SKU-AUDIO-001",
        "competitor_urls": [
            "https://example-competitor.com/product/abc",
            "https://example-competitor.com/product/xyz"
        ]
    }

    # 3. 初始化并运行核心工作流
    workflow = OmniSEOWorkflow(config)
    logger.info(f"开始处理任务 SKU: {mock_task['sku_id']}")
    
    results = workflow.run(mock_task)

    # 4. 保存结果
    output_dir = "data/output"
    os.makedirs(output_dir, exist_ok=True)
    
    if results:
        for lang, content in results.items():
            file_path = os.path.join(output_dir, f"{mock_task['sku_id']}_{lang}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        logger.info(f"✅ 任务完成，多语言 SEO 内容已保存至 {output_dir}")
    else:
        logger.error("❌ 任务失败，多次重写均未达到 Critic 设定的质量阈值。")

if __name__ == "__main__":
    main()
