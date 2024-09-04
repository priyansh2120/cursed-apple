import { Link, useNavigate } from "react-router-dom";
import { googleLogout } from '@react-oauth/google';

export default function Component() {
  const navigate = useNavigate()
  const logout = () => {
    localStorage.clear()
    googleLogout();
    navigate("/")
  }
  return (
    <div className="flex flex-col md:flex-row justify-between w-full px-4 py-4 text-[#432d1d]">
      <h1 className="text-3xl md:text-4xl font-bold font-conthrax">
      <span className="text-[#264653]">TRAVEL</span> <span className="text-black">EASE</span> 
      </h1>
      <div className="flex mt-2 md:mt-0 space-x-4 md:space-x-8 font-myriad mb-3 md:mb-0">
        <Link to="/chats" className="cursor-pointer text-sm md:text-lg  text-[#432d1d] hover:text-[#805f48] font-bold">
          CHAT
        </Link>
        <Link to="/" className="cursor-pointer text-sm md:text-lg hover:text-[#805f48] font-bold">
          ABOUT ME
        </Link>
        <p onClick={logout} className="text-sm md:text-lg hover:text-[#805f48] font-bold cursor-pointer">
          LOGOUT
        </p>
      </div>
    </div>

  )
}