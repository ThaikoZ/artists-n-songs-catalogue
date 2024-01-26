import Link from "next/link";
import { Menu } from "lucide-react";

const Navbar = () => {
  return (
    <div className="h-14 z-50 w-full border-b-2 border-grey-100 flex justify-between items-center align-middle text-center bg-white sticky top-0">
      <div className="flex container justify-between h-full px-2 ">
        <div className="flex items-center h-full  px-5">
          <Link href="/">
            <img
              src="/logo.png"
              alt="logo"
              className="h-8 min-w-fit cursor-pointer"
            />
          </Link>
        </div>
        <div className="flex h-full items-center  px-5 cursor-pointer md:hidden">
          <Menu />
        </div>
      </div>
    </div>
  );
};

export default Navbar;
