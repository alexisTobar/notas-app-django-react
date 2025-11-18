// Archivo: frontend/src/App.jsx

// --- 1. IMPORTACIONES ---
import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import CreationForm from './CreationForm.jsx';

// URL base de tu API de Django (donde está el ModelViewSet)
const API_URL = 'http://127.0.0.1:8000/api/notas/';

// --- 2. EL COMPONENTE PRINCIPAL 'App' ---

function App() {

  // --- 3. ESTADOS (MEMORIA) ---
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);

  // --- 4. FUNCIÓN PARA LEER NOTAS (R de CRUD) ---
  const fetchNotes = async () => {
    try {
      setLoading(true);
      const response = await axios.get(API_URL);
      // Aseguramos que la lista se cargue correctamente
      setNotes(response.data);
    } catch (error) {
      console.error("Error al cargar las notas:", error);
      // alert("Error: No se pudo conectar al servidor Django.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  // --- 5. FUNCIÓN PARA CREAR NOTAS (C de CRUD) ---
  const addNote = async (e, title, content) => {
    e.preventDefault();

    if (!title.trim() || !content.trim()) {
      alert("El título y el contenido no pueden estar vacíos.");
      return;
    }

    try {
      // Petición POST (Crear)
      const response = await axios.post(API_URL, {
        titulo: title,
        contenido: content,
        completada: false
      });

      // Actualizamos la lista de notas sin recargar la página.
      setNotes(prevNotes => [response.data, ...prevNotes]);

    } catch (error) {
      console.error("Error al crear la nota:", error);
      alert("Error al crear la nota.");
    }
  };

  // --- 6. FUNCIÓN PARA ELIMINAR NOTAS (D de CRUD) ---
  const deleteNote = async (id) => {
    // Usamos window.confirm ya que alert() no funciona en algunos entornos de desarrollo
    if (!window.confirm("¿Estás seguro de que quieres eliminar esta nota?")) {
      return;
    }

    try {
      // Petición DELETE (Borrar) - La URL debe incluir el ID
      await axios.delete(`${API_URL}${id}/`);

      // Eliminamos la nota de la lista local sin recargar.
      setNotes(prevNotes => prevNotes.filter(note => note.id !== id));

    } catch (error) {
      console.error("Error al eliminar la nota:", error);
      alert("Error al eliminar la nota.");
    }
  };

  // --- 7. FUNCIÓN PARA ALTERNAR ESTADO (U de CRUD) ---
  const toggleComplete = async (note) => {
    // 1. Preparamos el objeto con el estado opuesto
    const updatedNote = {
      ...note,
      completada: !note.completada
    };

    try {
      // Petición PATCH (Actualizar una parte) - La URL debe incluir el ID
      const response = await axios.patch(`${API_URL}${note.id}/`, updatedNote);

      // 2. Actualizamos la nota en la lista local sin recargar.
      setNotes(prevNotes =>
        prevNotes.map(n =>
          n.id === note.id ? response.data : n
        )
      );
    } catch (error) {
      console.error("Error al actualizar la nota:", error);
      alert("Error al actualizar la nota.");
    }
  };


  // --- 8. EL HTML (LO QUE SE DIBUJA) ---

  if (loading) {
    return <div className="container"><h1>Cargando notas...</h1></div>;
  }

  // --- DIBUJO FINAL ---
  return (
    <div className="container">
      <h1 className="header">Bloc de Notas Colaborativas</h1>

      <div className="notesGrid">

        {/* Componente Formulario de Creación */}
        <CreationForm onAddNote={addNote} />

        {/* Recorremos la lista de notas y creamos las tarjetas */}
        {notes.map(note => (
          <div
            key={note.id}
            className="noteCard"
            style={{
              opacity: note.completada ? 0.6 : 1,
              borderLeft: note.completada ? '5px solid #00C6FF' : '5px solid #333'
            }}
          >

            <h2 className="noteTitle">{note.titulo}</h2>
            <p className="noteContent">{note.contenido}</p>

            <div className="noteFooter">
              <span style={{ fontSize: '0.8rem' }}>
                Actualizado: {new Date(note.fecha_actualizacion).toLocaleDateString()}
              </span>

              <div>
                {/* Botón de Completar (U de CRUD) */}
                <button
                  onClick={() => toggleComplete(note)} // Pasamos la nota completa
                  style={{
                    padding: '5px 10px',
                    background: note.completada ? '#28a745' : '#ffc107',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px',
                    cursor: 'pointer',
                    marginRight: '10px'
                  }}
                >
                  {note.completada ? '✅ Completa' : '⏳ Pendiente'}
                </button>

                {/* Botón de Borrar (D de CRUD) */}
                <button
                  onClick={() => deleteNote(note.id)} // Pasamos SÓLO el ID
                  style={{
                    padding: '5px 10px',
                    background: '#dc3545',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px',
                    cursor: 'pointer'
                  }}
                >
                  Borrar
                </button>
              </div>
            </div>

          </div>
        ))}

        {notes.length === 0 && <p style={{ gridColumn: 'span 2', textAlign: 'center' }}>
          No hay notas creadas aún. ¡Usa el formulario para empezar!
        </p>}

      </div>
    </div>
  );
}

export default App;