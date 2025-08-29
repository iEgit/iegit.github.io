# iEgit Blog

This repository contains the source code for the iEgit blog, powered by Jekyll and hosted on GitHub Pages.

## Overview

This Jekyll blog includes:

- **Responsive design** with clean, professional styling
- **Blog post management** with categorization and archiving
- **SEO optimization** with meta tags and structured data
- **RSS feed** for content syndication
- **Sitemap** for search engine indexing
- **GitHub Pages compatibility** for easy deployment

## Structure

```
├── _config.yml          # Jekyll configuration
├── Gemfile              # Ruby dependencies
├── _layouts/            # Page templates
│   ├── default.html     # Base template
│   └── post.html        # Blog post template
├── _includes/           # Reusable components
│   ├── header.html      # Site header
│   └── footer.html      # Site footer
├── _posts/              # Blog posts (Markdown files)
├── _sass/               # SCSS stylesheets
│   ├── _base.scss       # Base styles
│   ├── _layout.scss     # Layout styles
│   └── _syntax-highlighting.scss # Code highlighting
├── assets/              # Static assets
│   └── css/
│       └── main.scss    # Main stylesheet
├── index.html           # Home page
├── about.md             # About page
└── archive.md           # Post archive page
```

## Local Development

### Prerequisites

- Ruby (version 2.7 or higher)
- Bundler gem

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/iEgit/iegit.github.io.git
   cd iegit.github.io
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Build the site:
   ```bash
   bundle exec jekyll build
   ```

4. Serve locally:
   ```bash
   bundle exec jekyll serve
   ```

5. Open your browser to `http://localhost:4000`

## Writing Posts

Create new blog posts in the `_posts/` directory using the following format:

### File naming
```
YYYY-MM-DD-post-title.md
```

### Post template
```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: category1 category2
author: Author Name
excerpt: "Brief description of the post content"
---

Your post content in Markdown format goes here...
```

## Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the main branch. No additional configuration is required.

### Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to the repository root containing your domain name
2. Configure your DNS provider to point to GitHub Pages
3. Enable HTTPS in repository settings

## Customization

### Styling
- Modify SCSS files in `_sass/` directory
- Main stylesheet is in `assets/css/main.scss`

### Layout
- Edit templates in `_layouts/` directory
- Modify components in `_includes/` directory

### Configuration
- Update `_config.yml` for site-wide settings
- Modify `Gemfile` for additional Jekyll plugins

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **SEO Optimized**: Meta tags, structured data, sitemap
- **Social Sharing**: Open Graph and Twitter Card support
- **RSS Feed**: Automatic feed generation for posts
- **Code Highlighting**: Syntax highlighting for code blocks
- **Archive Page**: Chronological listing of all posts
- **Category Support**: Organize posts by categories

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues:

- Create an issue on GitHub
- Email: your-email@example.com

---

Powered by [Jekyll](https://jekyllrb.com) and hosted on [GitHub Pages](https://pages.github.com)