# Doc2Book 📚

> 将文档网站转换为 PDF/EPUB 电子书的命令行工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## ✨ 功能特性

- 🕷️ **智能爬取**: 基于 Firecrawl 爬取文档网站，支持 JavaScript 渲染
- 📝 **Markdown 合并**: 自动整理页面顺序，生成结构化 Markdown
- 📄 **PDF 导出**: 使用 Pandoc + XeLaTeX 生成高质量 PDF
- 🔧 **CLI 友好**: 简洁的命令行界面，支持多种输出格式

## 🚀 快速开始

### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/bradenwu/doc2book.git
cd doc2book

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -e .
```

### 系统要求

- **Python** 3.10+
- **Pandoc** - [安装指南](https://pandoc.org/installing.html)
- **XeLaTeX** (可选，用于 PDF 导出) - [TeX Live](https://www.tug.org/texlive/)

### 配置 API Key

```bash
# 设置 Firecrawl API Key
export FIRECRAWL_API_KEY="your-api-key-here"
```

> 获取 API Key: [Firecrawl 官网](https://www.firecrawl.dev/)

## 📖 使用方法

### 基本用法

```bash
# 转换文档网站为 PDF
doc2book https://docs.example.com

# 指定输出文件名
doc2book https://docs.example.com -o mybook.pdf

# 只输出 Markdown
doc2book https://docs.example.com -f markdown

# 同时输出 PDF 和 Markdown
doc2book https://docs.example.com -f both

# 限制爬取页面数
doc2book https://docs.example.com -m 100
```

### 命令行参数

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--output` | `-o` | 输出文件路径 | `output.pdf` |
| `--format` | `-f` | 输出格式: pdf, markdown, both | `pdf` |
| `--max-pages` | `-m` | 最大爬取页面数 | `200` |

## 🏗️ 项目结构

```
doc2book/
├── cli/            # 命令行接口
│   └── main.py     # Typer CLI 入口
├── core/           # 核心逻辑
│   └── pipeline.py # 主处理流程
├── crawler/        # 爬虫模块
│   └── firecrawl.py# Firecrawl 爬虫
├── builder/        # 内容构建
│   └── markdown_builder.py # Markdown 合并
├── exporter/       # 导出模块
│   └── pdf_exporter.py     # PDF 导出
├── models/         # 数据模型
│   └── page.py     # Page 数据类
├── config/         # 配置
│   └── settings.py # 环境变量配置
└── utils/          # 工具函数
```

## 🔧 开发路线

### v0.1.0 (MVP) ✅
- [x] 基础 CLI 命令
- [x] Firecrawl 爬虫集成
- [x] Markdown 合并
- [x] PDF 导出 (Pandoc)

### v0.2.0 (计划中)
- [ ] EPUB 导出支持
- [ ] 进度条显示
- [ ] 断点续爬
- [ ] 自定义 CSS 样式

### v0.3.0 (未来)
- [ ] 多语言文档支持
- [ ] 图片本地化
- [ ] 目录自动生成
- [ ] 配置文件支持

## 🤝 贡献指南

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- [Firecrawl](https://www.firecrawl.dev/) - 强大的网页爬取 API
- [Pandoc](https://pandoc.org/) - 通用文档转换工具
- [Typer](https://typer.tiangolo.com/) - 优秀的 CLI 框架

---

**Made with ❤️ by Braden Wu**
