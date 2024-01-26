import axios from "axios";

export const baseURL =
  process.env.REACT_APP_API_URL || "http://localhost:8000/api";

const axiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://localhost:8000/api",
});

export default axiosInstance;
