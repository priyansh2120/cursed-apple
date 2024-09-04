import interactive from "../assets/interactive.png";
import personalize from "../assets/personalize.png";
import seamless from "../assets/seamless.png";
import accuracy from "../assets/accuracy.png";

export default function Component({ keyname }) {
  let data = {
    "Personalized Itineraries": {
      img: personalize,
      message: "Receive uniquely crafted dating itineraries that align perfectly with your preferences, making every moment special."
    },
    "Instant Recommendations": {
      img: interactive,
      message: "Leveraging powerful data processing and advanced vector search, the system instantly provides the most up-to-date suggestions."
    },
    "Seamless Interaction": {
      img: seamless,
      message: "Effortlessly request and receive comprehensive itineraries through an interface designed for smooth, user-friendly interaction."
    },
    "Enhanced Precision": {
      img: accuracy,
      message: "Combining LLMs, embeddings, and real-time data, our recommendations are both precise and contextually aware."
    }
  };
  
  return (
    <div className="py-4 gap-1.5 flex-1 flex flex-col justify-center md:items-center">
  <div className="flex justify-center items-center gap-2 bg-[#362315] bg-opacity-30 p-4 rounded-md">
    <img className="w-16 h-16" src={data[keyname].img} alt="huh" />
    <p className="text-md font-conthrax text-#264653">{keyname}</p>
  </div>
  <p className="font-myriad mb-2 text-justify text-[#393708] bg-[#362315] bg-opacity-20 p-4 rounded-md">
    {data[keyname].message}
  </p>
</div>

  );
}
