# Development Guide with Hot Reloading

## Quick Start with Watch Mode

Start the services with hot-reloading enabled:

```bash
docker compose watch
```

This will:
- **Frontend**: Sync changes from `src/` and `public/` directories in real-time
- **Backend**: Auto-restart Flask when you change Python files
- Watch for `package.json` changes and rebuild when needed

## What Gets Hot-Reloaded

### Frontend (React)
- ✅ Changes to `.jsx`, `.js`, `.css` files in `src/`
- ✅ Changes to files in `public/`
- 🔄 Rebuilds automatically when `package.json` changes

### Backend (Flask)
- ✅ Changes to `.py` files
- ✅ Auto-restart with Flask debug mode
- ✅ All Python code changes apply instantly

## Usage

### Start with Watch Mode
```bash
docker compose watch
```

### Regular Production Build
```bash
docker compose up -d --build
```

### Stop Services
```bash
docker compose down
```

## How It Works

The `watch` configuration uses three actions:

1. **`sync`**: Copies changed files into the container (fast)
2. **`sync+restart`**: Syncs files and restarts the service
3. **`rebuild`**: Triggers a full rebuild (for package.json changes)

## Notes

- Frontend changes sync to the built static files in nginx
- Backend mounts the entire `/backend` directory as a volume
- Flask runs with `FLASK_DEBUG=1` for auto-reloading
- Changes appear within 1-2 seconds

## Troubleshooting

If changes aren't appearing:
```bash
docker compose down
docker compose watch
```

To see logs:
```bash
docker compose logs -f frontend
docker compose logs -f backend
```
