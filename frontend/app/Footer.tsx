import { Label } from "@/components/ui/label";
import React from "react";

const Footer = () => {
  return (
    <footer
      className="w-full bg-white text-center p-4 text-gray-600  border-t-2 border-gray-100 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-700 
    "
    >
      <Label>© {new Date().getFullYear()} Muzicat. All rights reserved.</Label>
    </footer>
  );
};

export default Footer;
