import { useEffect, useState } from 'react'

function App() {
  const [health, setHealth] = useState('Checking backend...')

  useEffect(() => {
    fetch('/api/health')
      .then((response) => response.json())
      .then((data: { status: string; database: string }) => {
        setHealth(`${data.status} / database ${data.database}`)
      })
      .catch(() => setHealth('Backend unavailable'))
  }, [])

  return (
    <main>
      <h1>Leadgen AI</h1>
      <p>Frontend is connected to the backend.</p>
      <output>{health}</output>
    </main>
  )
}

export default App
