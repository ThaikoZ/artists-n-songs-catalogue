import { Button } from "@/components/ui/button";
import { Song, columns } from "./utils/columns";
import { DataTable } from "./DataTable";
import { Input } from "@/components/ui/input";
import Link from "next/link";
import ContentCard from "./components/ContentCard";
import axiosInstance, { baseURL } from "./services/api-client";

// Hamburger menu
async function getData(): Promise<Song[]> {
  const data = await axiosInstance
    .get("/songs/")
    .then((res) => res.data)
    .catch((err) => console.log(err));
  return data || [];
}

export default async function HomePage() {
  const data = await getData();

  return (
    <ContentCard>
      <div className="flex gap-3 ">
        <Link href="/add">
          <Button className="bg-blue-600 hover:bg-blue-500 w-fit min-w-32 ">
            Add song
          </Button>
        </Link>
        <Input placeholder="Search..." />
      </div>
      <div className="w-full ">
        <DataTable columns={columns} data={data} />
      </div>
      {/* TODO: Edit, Delete buttons */}
    </ContentCard>
  );
}
