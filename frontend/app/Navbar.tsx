import React, { PropsWithChildren } from "react";
import Image from "next/image";
import { Menu } from "lucide-react";
import { ModeToggle } from "@/components/ui/mode-toggler";
const Navbar = () => {
  return (
    <div className="h-14 w-full border-b-2 border-grey-100 flex justify-between items-center align-middle text-center bg-white mb-12">
      <div className="flex container justify-between h-full px-2 ">
        <div className="flex items-center h-full pt-1 px-5 ">
          <p className="text-xl font-semibold">Muzicat</p>
        </div>
        <div className="flex h-full items-center  px-5 cursor-pointer">
          {/* <ModeToggle /> */}
        </div>
      </div>
    </div>
  );
};

export default Navbar;
