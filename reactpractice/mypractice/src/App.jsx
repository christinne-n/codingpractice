import {useState} from 'react';

export default function App() {
  const[count, setCount] = useState(0);


return (
  <main style = {{padding: 16 }}>
    <h1> Click counter </h1>
    <p> You clicked {count} times.</p>
    <button onClick= { () => setCount ( (count) => count + 1)}>
      Click me!
    </button>
  </main>
  );
}