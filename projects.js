// The register. Add a project by adding an object here — that's the whole framework.
//
// Fields:
//   name    (required)  project name
//   desc    (required)  one sentence on what it does and why you use it
//   url     (optional)  link to repo or site
//   since   (optional)  year it entered use
//   status  (optional)  "in use" (default) or "dormant"
//   lang    (optional)  primary language
//   tags    (optional)  array of short labels

window.PROJECTS = [
  {
    name: "iusethis.org",
    desc: "This site — a continuous-form register of projects, served as a single static page from GitHub Pages.",
    url: "https://github.com/USERNAME/iusethis.org",
    since: "2026",
    status: "in use",
    lang: "HTML",
    tags: ["static", "github pages"],
  },
  {
    name: "example-project",
    desc: "Replace me: a sample record showing every field the register understands.",
    url: "https://example.com",
    since: "2024",
    status: "dormant",
    lang: "C",
    tags: ["sample", "delete me"],
  },
];
