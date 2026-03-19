# 使用示例

本文档展示 Doc2Book 的常见使用场景。

## 基本用法

### 1. 转换文档网站为 PDF

```bash
# 设置 API Key
export FIRECRAWL_API_KEY="your-api-key"

# 转换文档
doc2book https://docs.python.org/3/
```

### 2. 指定输出文件名

```bash
doc2book https://fastapi.tiangolo.com/ -o fastapi-docs.pdf
```

### 3. 只生成 Markdown

```bash
doc2book https://vuejs.org/guide/ -f markdown
```

### 4. 限制爬取页面数

```bash
# 只爬取前 50 页
doc2book https://react.dev/learn -m 50
```

## 高级用法

### 批量转换脚本

```bash
#!/bin/bash
# batch_convert.sh

docs=(
  "https://docs.python.org/3/"
  "https://fastapi.tiangolo.com/"
  "https://vuejs.org/guide/"
)

for url in "${docs[@]}"; do
  name=$(echo "$url" | sed 's/https:\/\///' | sed 's/\//-/g')
  doc2book "$url" -o "${name}.pdf"
done
```

### 作为 Python 模块使用

```python
from doc2book.core.pipeline import run_pipeline

result = run_pipeline(
    url="https://docs.example.com",
    output_dir="./output",
    output_name="my-docs",
    max_pages=100,
    format="both"  # pdf + markdown
)

print(f"Markdown: {result['markdown']}")
print(f"PDF: {result['pdf']}")
```

## 常见文档网站

| 网站 | 命令示例 |
|------|----------|
| Python 官方文档 | `doc2book https://docs.python.org/3/` |
| FastAPI 文档 | `doc2book https://fastapi.tiangolo.com/` |
| Vue.js 文档 | `doc2book https://vuejs.org/guide/` |
| React 文档 | `doc2book https://react.dev/learn` |

## 故障排除

### API Key 问题

```bash
# 检查 API Key 是否设置
echo $FIRECRAWL_API_KEY

# 临时设置
export FIRECRAWL_API_KEY="fc-xxxxx"
```

### Pandoc 未安装

```bash
# Ubuntu/Debian
sudo apt-get install pandoc

# macOS
brew install pandoc

# 验证安装
pandoc --version
```

### XeLaTeX 未安装（PDF 需要）

```bash
# Ubuntu/Debian
sudo apt-get install texlive-xetex

# macOS
brew install --cask mactex
```
