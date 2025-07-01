# Architect

A modern SaaS-style Svelte application with a clean, subtle design featuring a sidebar navigation and collaborative blackboard functionality.

## Features

- **Modern SaaS Design**: Clean, subtle styling with a professional look and feel
- **Responsive Layout**: Sidebar navigation that adapts to mobile devices
- **Dashboard**: Overview page with key metrics and recent activity
- **Blackboard**: Collaborative workspace for team notes and ideas
- **TypeScript Support**: Full TypeScript integration for better development experience

## Project Structure

```
src/
├── routes/
│   ├── +layout.svelte      # Main layout with sidebar and header
│   ├── +page.svelte        # Dashboard page
│   └── blackboard/
│       └── +page.svelte    # Blackboard page
├── app.css                 # Global styles
└── app.html               # HTML template
```

## Pages

### Dashboard (`/`)
- Overview cards showing key metrics
- Recent activity feed
- Quick access to main features

### Blackboard (`/blackboard`)
- Collaborative note-taking workspace
- Color-coded notes
- Add, edit, and delete functionality
- Real-time updates

## Getting Started

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start development server**:
   ```bash
   npm run dev
   ```

3. **Open in browser**:
   Navigate to `http://localhost:5173`

## Development

- **Build for production**:
  ```bash
  npm run build
  ```

- **Preview production build**:
  ```bash
  npm run preview
  ```

## Design System

The application uses a subtle, modern design system with:
- Clean typography using system fonts
- Subtle shadows and borders
- Consistent spacing and colors
- Responsive grid layouts
- Hover effects and transitions

## Technologies

- **SvelteKit**: Full-stack framework
- **TypeScript**: Type safety
- **CSS**: Custom styling with modern features
- **Vite**: Build tool and dev server
