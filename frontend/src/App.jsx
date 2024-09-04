import './App.css'
import { Outlet } from "react-router-dom";
import { GoogleOAuthProvider } from '@react-oauth/google';
import "./firebase"
import { useEffect, useState } from 'react';

function App() {
  const [firstRender, setFirstRender] = useState(true)
  useEffect(() => {
    if (firstRender) {
      console.clear()
      setFirstRender(false)
    }
  }, [])
  return (
    <GoogleOAuthProvider clientId= {import.meta.env.GOOGLE_CLIENT_ID} >
      <section className=''>
        <Outlet />
      </section>
    </GoogleOAuthProvider>
  )
}

export default App
