
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyAW3vTRn4YFGvvQg1AM7Ntv5sXoxxY2EZA",
  authDomain: "travel-itinerary-rag.firebaseapp.com",
  projectId: "travel-itinerary-rag",
  storageBucket: "travel-itinerary-rag.appspot.com",
  messagingSenderId: "1026770078819",
  appId: "1:1026770078819:web:4f478837f666ed1c793c56",
  measurementId: "G-XQZ2FRFFXL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const analytics = getAnalytics(app);