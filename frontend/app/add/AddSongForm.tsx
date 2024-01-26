"use client";
import React from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import zod from "zod";
import { useForm } from "react-hook-form";
import axiosInstance from "../services/api-client";
import { Loader2 } from "lucide-react";
import { useRouter } from "next/navigation";

interface FormValues {
  title: string;
  album_title: string;
  artists: string;
  duration_in_seconds: number;
  sold_copies: number;
}

const schema = zod.object({
  title: zod
    .string()
    .min(1, { message: "Title must be at least 1 character long" }),
  album_title: zod.string().optional(),
  artists: zod.string().min(1, { message: "Authors field shouldn't be empty" }),
  duration_in_seconds: zod
    .string()
    .min(1, { message: "Duration must be at least 1 second" }),
  sold_copies: zod
    .string()
    .min(0, { message: "Sold copies must be at least 0" }),
});

const AddSongForm = () => {
  const { register, handleSubmit } = useForm<FormValues>();
  const [error, setError] = React.useState<string>("");
  const [isLoading, setLoading] = React.useState<boolean>(false);
  const router = useRouter();

  const onSubmit = (data: FormValues) => {
    const validation = schema.safeParse(data);
    if (!validation.success) {
      setError(validation.error.errors[0].message);
      return;
    }
    setLoading(true);

    const payload = {
      title: data.title,
      album_title: data.album_title,
      artists: data.artists.split(",").map((artist) => artist.trim()),
      duration_in_seconds: parseInt(data.duration_in_seconds.toString()),
      sold_copies: parseInt(data.sold_copies.toString()),
    };

    // Who knows why, but axios doesn't work with react-hook-form
    axiosInstance
      .post("/songs", payload)
      .then((response) => {
        router.push("/");
        console.log("success");
      })
      .catch((error) => {
        console.log(error.response);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      onChange={() => setError("")}
      className="flex flex-col gap-4 w-full  justify-center"
    >
      <div className="flex gap-3 flex-col sm:flex-row">
        <div className="grid w-full items-center gap-1.5">
          <Label htmlFor="title">Title</Label>
          <Input {...register("title")} id="title" placeholder="Song title" />
        </div>
        <div className="grid w-full items-center gap-1.5">
          <Label htmlFor="album_title">Album name</Label>
          <Input
            {...register("album_title")}
            id="album_title"
            placeholder="Album name (optional)"
          />
        </div>
      </div>
      <div className="grid w-full items-center gap-1.5">
        <Label htmlFor="artists">Authors</Label>
        <Input {...register("artists")} id="artists" placeholder="Authors" />
      </div>
      <div className="flex gap-3 flex-col sm:flex-row">
        <div className="grid w-full items-center gap-1.5">
          <Label htmlFor="duration_in_seconds">Duration in seconds</Label>
          <Input
            {...register("duration_in_seconds")}
            id="duration_in_seconds"
            type="number"
            min="0"
            max="1000"
            placeholder="(180 is 3min)"
          />
        </div>

        <div className="grid w-full items-center gap-1.5">
          <Label htmlFor="sold_copies">Sold copies</Label>
          <Input
            {...register("sold_copies")}
            id="sold_copies"
            type="number"
            min="0"
            max="100000000"
            placeholder="0"
            defaultValue={0}
          />
        </div>
      </div>
      <div className="flex justify-between items-center mt-3">
        <Label className="text-red-600 w-fit">{error}</Label>
        <Button type="submit" disabled={isLoading} className="w-full sm:w-36">
          {isLoading && <Loader2 className="mr-2 h-6 w-6 animate-spin" />}
          Add song
        </Button>
      </div>
    </form>
  );
};

export default AddSongForm;
