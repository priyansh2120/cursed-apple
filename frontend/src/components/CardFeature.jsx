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
    <div className="py-4 gap-1.5 border-gradient flex-1 flex flex-col justify-center md:items-center">
      <div className="flex justify-center items-center gap-2 ">
        <img className="w-16 h-16" src={data[keyname].img}  alt="huh"/>
        <p className="text-md font-conthrax">{keyname}</p>
      </div>
      <p className="font-myriad mb-2 text-justify">{data[keyname].message}</p>
    </div>
  );
}
