import { Link } from "react-router-dom";

export default function Component({ loading, login }) {
  return (
    <header className="w-full py-4 flex justify-between items-center font-bold">
      <nav className="flex justify-center items-center gap-4 m-auto">
        <a
          href="#aboutus"
          className="hover:text-[#805f48] block text-[#432d1d] text-lg cursor-pointer px-2"
        >
          ABOUT ME
        </a>
        <a
          href="#demo"
          className="hover:text-[#805f48] text-[#432d1d] text-lg cursor-pointer px-2"
        >
          DEMO
        </a>
        {localStorage.getItem("email") && localStorage.getItem("access_token") ? (
          <Link
            className="hover:text-[#805f48] text-[#432d1d] text-lg cursor-pointer px-2"
            to="/chats"
          >
            CHAT
          </Link>
        ) : (
          <p
            onClick={login}
            className={
              loading
                ? "text-[#805f48] text-lg cursor-pointer px-2"
                : "hover:text-[#805f48] text-[#432d1d] text-lg cursor-pointer px-2"
            }
          >
            {loading ? "PLEASE WAIT" : "LOGIN/REGISTER"}
          </p>
        )}
      </nav>
    </header>
  );
}
