import React, { useState } from "react";
import BannerGlobe from "../components/BannerGlobe"
import AboutUs from "../components/AboutUs"
import HeaderHome from "../components/HeaderHome"
import CardFeature from "../components/CardFeature"
import SimpleFooter from "../components/SimpleFooter"
import { useNavigate } from "react-router-dom";
import { useGoogleLogin } from '@react-oauth/google';
import axios from "axios";

const HangoutAI = () => {
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)
  const login = useGoogleLogin({
    onSuccess: async response => {
      setLoading(true)
      let { data } = await axios({
        method: "POST",
        url: "http://localhost:3001/social-login",
        data: {
          access_token: response.access_token
        }
      })
      let { access_token, user } = data
      localStorage.setItem("access_token", access_token)
      localStorage.setItem("name", user.name)
      localStorage.setItem("email", user.email)
      localStorage.setItem("image", user.image)
      localStorage.setItem("createdAt", user.createdAt)
      setLoading(false)
      navigate("/chats");
    }
  });
  return (
    <div className="font-myriad min-h-screen bg-[url('https://i.imgur.com/c89MDBb.jpeg')] flex flex-col items-center md:pt-12 pt-8 px-4 md:px-0">
      <HeaderHome loading={loading} login={login} />
      <BannerGlobe login={login} />
      <div className="flex flex-col   sm:w-[80%] md:w-[640px]">
        <AboutUs />
        <div className="flex flex-col md:flex-row gap-8">
          <CardFeature keyname={"Personalized Itineraries"} />
          <CardFeature keyname={"Instant Recommendations"} />
        </div>
        <div className="flex flex-col md:flex-row gap-8">
          <CardFeature keyname={"Seamless Interaction"} />
          <CardFeature keyname={"Enhanced Precision"} />
        </div>
      </div >
      <SimpleFooter />
    </div >
  );
};

export default HangoutAI;
