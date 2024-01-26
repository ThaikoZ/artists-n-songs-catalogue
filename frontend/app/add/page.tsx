import React from "react";
import ContentCard from "../components/ContentCard";
import { Label } from "@/components/ui/label";
import Image from "next/image";
import AddSongForm from "./AddSongForm";

const AddPage = () => {
  return (
    <ContentCard>
      <div className="flex flex-col md:flex-row gap-2">
        <div className="hidden lg:flex w-full justify-center items-center ">
          <Image
            src="/add-image.jpg"
            width="350"
            height="350"
            alt="Vinyl"
            className="rounded-lg"
          />
        </div>
        <div className="flex flex-col gap-4 w-full  justify-center px-5 py-10 ">
          <Label className="w-full  font-bold text-4xl text-zinc-950 mb-4">
            Add a New Song!
          </Label>
          <AddSongForm />
        </div>
      </div>
    </ContentCard>
  );
};

export default AddPage;
