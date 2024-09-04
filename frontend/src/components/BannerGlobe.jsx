
import { useNavigate } from "react-router-dom";

export default function Component({ login }) {
  const navigate = useNavigate()
  const actionGlobe = () => {
    if (localStorage.getItem("access_token")) {
      navigate("/chats")
    } else {
      login()
    }
  }
  return (
    <>
      <div className="text-center mt-10 cursor-pointer bg-[url('https://i.imgur.com/trZs8Ty.png')]">
        <h1 className="text-5xl sm:max-w-[320px] md:max-w-[80%] font-bold font-conthrax m-auto "><span className="text-[#264653]">TRAVEL EASE</span></h1>
        <p className="text-xl mt-8 max-w-[300px] md:max-w-full m-auto">
          Plan your next adventure effortlessly with Travel Ease.<br />Tailor your trips to perfection using our intelligent travel assistant.
        </p>
      </div>
      <img src="https://i.imgur.com/trZs8Ty.png" alt = "Globe"  />
     
    </>
  )
}