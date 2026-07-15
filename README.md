# KeyGuard: API Key Manager
<div align = "center">
    
KeyGuard is a lightweight, secure, and elegant API key management system built with Flask and SQLite. It provides a beautiful interface to generate, track, and revoke API keys, along with a simple REST endpoint for validation.
</div>
     
## 🚀 Features            
    
- **Key Generation**: Create unique UUID-based API keys with custom labels.
- **Key Validation**: Simple GET endpoint to verify key validity.
- **Dashboard**: Premium dark-mode UI for managing active keys.
- **Revocation**: Instantly deactivate keys with a single click.
- **SQLite Backend**: Lightweight and portable data storage.
      
## 🛠️ Tech Stack                        
     
- **Backend**: Flask, Flask-SQLAlchemy (SQLite)
- **Frontend**: Vanilla HTML/CSS (Premium Glassmorphism Design)
- **Icons**: Lucide-inspired SVG icons
- **Fonts**: Inter (Google Fonts)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/[YOUR_USERNAME]/flask-api-key-manager.git
   cd flask-api-key-manager
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```
   The dashboard will be available in your localhost port.

## 🔌 API Reference

### Validate an API Key

Verify if an API key is valid and active.

- **Endpoint**: `/api/validate`
- **Method**: `GET`
- **Query Parameters**:
  - `key` (required): The API key to validate.

**Response (Success)**:
```json
{
  "valid": true,
  "name": "Production Client"
}
```

**Response (Failure)**:
```json
{
  "valid": false,
  "error": "Invalid or revoked key"
}
```

## 🎨 Design Philosophy

KeyGuard was built with a focus on **Premium Aesthetics**.
- **Dark Mode**: Reduces eye strain and looks professional.
- **Glassmorphism**: Subtle blurs and translucent borders for a modern feel.
- **Responsive**: Works perfectly on mobile, tablet, and desktop.
- **Micro-interactions**: Hover states and scale transitions for a tactile feel.

---

Built with ❤️ by Antigravity
