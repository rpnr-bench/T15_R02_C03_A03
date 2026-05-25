const config = {
  title: 'Clean Docusaurus Benchmark',
  tagline: 'Documentation maintenance benchmark',
  favicon: 'img/favicon.ico',
  url: 'https://example.com',
  baseUrl: '/',
  organizationName: 'cs552-mcp-agent-security',
  projectName: 'clean-docusaurus-benchmark',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  presets: [
    ['classic', { docs: { sidebarPath: require.resolve('./sidebars.js') }, blog: false }]
  ]
};
module.exports = config;
