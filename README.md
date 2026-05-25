# Versioned Documentation Site

A Docusaurus site that keeps current and versioned documentation aligned across releases.

## Project layout

- `docs/` — Current documentation pages.
- `versioned_docs/` — Version-specific documentation snapshots.
- `versions.json` — Published documentation versions.
- `sidebars.js` — Navigation for current docs.

## Quick start

```bash
make validate
```
```bash
npm install
```
```bash
npm run build
```

## Documentation workflow

1. Add or update Markdown pages under `docs/`.
2. Keep `sidebars.js` synchronized with new pages.
3. Validate JavaScript config before opening a PR.
4. Run a full Docusaurus build before release.

## Maintenance notes

Keep release notes and version links consistent across current and versioned docs.

## Contributing

Keep changes focused, update documentation when behavior changes, and run the validation commands before submitting a pull request.
