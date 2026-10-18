# Site design

The site should feel like W3Schools: flat, plain, quick to scan, with the content doing the work. It should not look like a generic AI-generated site. The styles live in `docs/stylesheets/site.css`; the two scripts that change the page are `docs/javascripts/prevnext.js` and `docs/javascripts/progress.js`.

## Layout

- A white header with the site title, the light/dark toggle, search and the GitHub link.
- A dark bar of subject tabs under the header (`#282a35`, white uppercase labels). The current tab has a light gray background with dark text. Tab labels are short (Proofs, University, Finance) so they fit on one line on a laptop.
- A light gray left sidebar (`#ebedee`) listing the chapters and lessons of the current tab. The current lesson is white with a green left border.
- The page title is large and light (weight 400). Section headings are plain and smaller.
- Under every page title there is an outlined "Previous" button on the left and a green "Next" button on the right (`#04aa6d`). The same pair repeats at the bottom of the page.
- The home page is a table of contents, like the first page of a book.

## Boxes

| Box | Look | Markdown |
|---|---|---|
| Worked example | Gray background, 5px corners | `<div class="example" markdown>` |
| Note | Pale yellow, no icon | `<div class="note" markdown>` |
| Warning | Pale red with a red left border, no icon | `<div class="warning" markdown>` |
| Solution | White, thin border, green left border, collapsible | `<details class="solution" markdown>` |
| In code | Same as a solution | `<details class="code" markdown>` |

## Colour

One dark colour (the tab bar and footer), one accent (green), and gray neutrals. Links are dark green and underlined. Inline code is dark red on light gray. Dark mode uses the same layout with dark grays and a slightly lighter green; no neon and no glow.

## Things to avoid

These are common signs of AI-generated web design. Don't add any of them.

- Gradients of any kind, glow or aurora backgrounds, glass blur effects, neon colours on dark backgrounds.
- Purple, indigo or violet anywhere (the default colour of many generators).
- Emoji used as icons, bullets or headings. Use the theme's built-in icons sparingly, or none.
- A centered "hero" section with a pill badge, a big tagline and three feature cards with icons, followed by a call-to-action button.
- The Inter or Geist fonts. The site uses the system font stack, like W3Schools (Segoe UI on Windows, the system font on phones).
- Drop shadows, heavily rounded corners (more than 5px), and cards nested inside cards.
- Marketing language in any site text: "unlock", "elevate", "master", "supercharge", "your journey", "level up".
- Giving every element the same visual weight. The title leads, then headings, then body text.

## Checking a change

Run `zensical serve`, then look at a lesson page at desktop width (about 1400px) and phone width (about 390px), in light and dark mode. Check that math renders, solutions open and close, the tabs fit, and the Previous and Next buttons appear.
