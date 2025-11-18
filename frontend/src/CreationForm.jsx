// Archivo: frontend/src/CreationForm.jsx
import React, { useState } from 'react';

// Este componente ahora maneja sus propios estados (newNoteTitle, newNoteContent)
function CreationForm({ onAddNote }) { // Recibe la función 'addNote' como prop 'onAddNote'
    const [newNoteTitle, setNewNoteTitle] = useState('');
    const [newNoteContent, setNewNoteContent] = useState('');

    // La función local que maneja el envío
    const handleSubmit = (e) => {
        // Llama a la función que le pasaron desde App.jsx
        onAddNote(e, newNoteTitle, newNoteContent);
        // Limpiamos los estados DESPUÉS de que App.jsx lo procese
        setNewNoteTitle('');
        setNewNoteContent('');
    };

    return (
        // Usa el handleSubmit para el formulario
        <form onSubmit={handleSubmit} className="noteCard">
            <h3 style={{ color: '#00C6FF', marginBottom: '15px' }}>Crear Nueva Nota</h3>
            <input
                type="text"
                placeholder="Título de la nota"
                value={newNoteTitle}
                // Actualiza su estado local (no el de App)
                onChange={(e) => setNewNoteTitle(e.target.value)}
                style={{ padding: '10px', marginBottom: '10px', border: '1px solid #444', backgroundColor: '#333', color: '#f4f7f6', borderRadius: '4px' }}
            />
            <textarea
                placeholder="Contenido..."
                value={newNoteContent}
                onChange={(e) => setNewNoteContent(e.target.value)}
                style={{ padding: '10px', marginBottom: '15px', border: '1px solid #444', backgroundColor: '#333', color: '#f4f7f6', borderRadius: '4px', minHeight: '100px' }}
            />
            <button
                type="submit"
                style={{ padding: '10px', background: '#007BFF', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}
            >
                Guardar Nota
            </button>
        </form>
    );
}

export default CreationForm;