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
    <GoogleOAuthProvider clientId="1091646798667-prjuivp5pla0r1rcq4dboc19pau5k818.apps.googleusercontent.com">
      <section className=''>
        <Outlet />
      </section>
    </GoogleOAuthProvider>
  )
}

export default App
