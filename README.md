# My (Git-JSON) Resume!

A fully automated resume pipeline (with GitHub Actions) that generates beautiful PDF and HTML resumes from a simple JSON file using [JSON Resume](https://jsonresume.org/) and [GitHub Actions](https://docs.github.com/en/actions). Push changes to your `resume.json` and your resume automatically updates!

## 🌟 Features

- **JSON-Powered**: Store your resume in a structured, version-controlled JSON format
- **Automated Builds**: GitHub Actions automatically generates PDF and HTML versions
- **Free Hosting**: GitHub Pages serves your resume online for free
- **Multiple Profiles**: Create tailored resumes in `profiles/` directories for different job types
- **Beautiful Theme**: Uses the [jsonresume-theme-macea](https://www.npmjs.com/package/jsonresume-theme-macea) theme
- **One-Page PDF**: Automatically trims PDFs to one page for cleaner presentation

## 🚀 Quick Start - Fork This Repo

1. **Fork this repository** to your GitHub account
2. **Update `resume.json`** with your information (see the existing file for an example)
3. **Enable GitHub Pages**:
   - Go to your forked repo's Settings → Pages
   - Set Source to "Deploy from a branch"
   - Select branch: `master`, folder: `/ (root)`
   - Click Save
4. **Push your changes** to the `master` branch
5. **Wait for the Action to complete** (check the Actions tab)
6. **View your resume** at `https://your-username.github.io/your-repo-name/`

## 📝 Customizing Your Resume

### Editing resume.json

Your resume data lives in `resume.json` at the root level. Follow the [JSON Resume Schema](https://jsonresume.org/schema/) for the complete specification. The existing file serves as a working example.

Key sections:

- `basics`: Name, contact info, profiles (LinkedIn, GitHub, etc.)
- `work`: Work experience
- `education`: Educational background
- `skills`: Technical and professional skills
- `projects`: Personal or professional projects
- `awards`: Awards and recognition (optional)
- `certificates`: Certifications (optional)

### Creating Tailored Resumes (Profiles)

Create different versions of your resume for different applications:

```bash
mkdir -p profiles/job-type
cp resume.json profiles/job-type/resume.json
# Edit profiles/job-type/resume.json with tailored content
```

Then manually generate that profile's resume using resume-cli (see below).

### Changing the Theme

The project uses `jsonresume-theme-macea` by default. To use a different theme:

1. Browse available themes at [JSON Resume Themes](https://jsonresume.org/themes/)
2. Update `.github/workflows/build_resume.yaml` (lines 24-25, 30-31) with your theme name
3. Update `package.json` with the new theme dependency
4. Push changes and let GitHub Actions rebuild

## 🛠️ Local Development

Install dependencies:

```bash
npm install -g resume-cli
npm install
```

Generate your resume locally:

```bash
# Generate HTML
resume export --theme=jsonresume-theme-macea resume.html

# Generate PDF
resume export --theme=jsonresume-theme-macea resume.pdf
```

## 📚 How It Works

1. You edit `resume.json` with your resume data
2. Push changes to the `master` branch
3. GitHub Actions workflow triggers:
   - Installs resume-cli and the theme
   - Generates HTML and PDF files
   - Trims PDF to one page using Python script
   - Commits generated files back to the repo
4. GitHub Pages serves the `index.html` file at your site URL

## 📄 Example Resume

This repo includes a complete working example in `resume.json` - use it as a reference for formatting and structure!

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have ideas for improvements!

## 📜 License

Feel free to fork and customize this project for your own use!
