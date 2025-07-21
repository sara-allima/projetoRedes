import { useEffect, useState } from "react";

function App() {
  const [tarefas, setTarefas] = useState([]);

  useEffect(() => {
    fetch("http://44.201.100.45/:8000/tarefas/api/")
      .then((res) => res.json())
      .then((data) => {
        console.log("Dados recebidos:", data);
        setTarefas(data);
      })
      .catch((erro) => console.error("Erro ao buscar tarefas:", erro));
  }, []);

  return (
    <div>
      <h1>Tarefas</h1>
      <ul>
        {tarefas.map((tarefa) => (
          <li key={tarefa.id}>{tarefa.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
