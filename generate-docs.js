// generate-docs.js
const fs = require("fs");
const path = require("path");

const sectionsDir = path.join(__dirname, "sections");
const outputFile = path.join(__dirname, "docs.md");

const sectionFiles = fs
  .readdirSync(sectionsDir)
  .filter(f => f.endsWith(".md"))
  .sort();

let combined = "";

sectionFiles.forEach(file => {
  const content = fs.readFileSync(path.join(sectionsDir, file), "utf8");
  combined += `<!-- FILE: ${file} -->\n\n`;
  combined += content.trim() + "\n\n";
});

fs.writeFileSync(outputFile, combined.trim());
console.log("✅ Combined docs written to docs.md");
