import uuid
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keys.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class APIKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(36), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "key": self.key,
            "name": self.name,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "is_active": self.is_active
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    keys = APIKey.query.order_by(APIKey.created_at.desc()).all()
    return render_template('index.html', keys=keys)

@app.route('/generate', methods=['POST'])
def generate_key():
    name = request.form.get('name', 'Default Key')
    new_key = str(uuid.uuid4())
    api_key = APIKey(key=new_key, name=name)
    db.session.add(api_key)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/revoke/<int:key_id>', methods=['POST'])
def revoke_key(key_id):
    api_key = APIKey.query.get_or_404(key_id)
    db.session.delete(api_key)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/validate', methods=['GET'])
def validate_key():
    key_to_check = request.args.get('key')
    if not key_to_check:
        return jsonify({"valid": False, "error": "No key provided"}), 400
    
    api_key = APIKey.query.filter_by(key=key_to_check, is_active=True).first()
    if api_key:
        return jsonify({"valid": True, "name": api_key.name}), 200
    else:
        return jsonify({"valid": False, "error": "Invalid or revoked key"}), 401

if __name__ == '__main__':
    app.run(debug=True)
