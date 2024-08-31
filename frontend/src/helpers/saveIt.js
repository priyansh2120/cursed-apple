import axios from "axios";
export default async function saveIt(id, messages) {
  try {
    let res = await axios({
      method: "POST",
      url: "http://localhost:3001/chats/" + id,
      headers: {
        access_token: localStorage.getItem("access_token")
      },
      data: {
        messages
      }
    })
  } catch (error) {
    console.log(error);
  }
}