import { Button } from "@/components/ui/button";
import { Product, columns } from "./columns";
import { DataTable } from "./DataTable";
import { Input } from "@/components/ui/input";
import axios from "axios";

// Hamburger menu

async function getData(): Promise<Product[]> {
  const data = await axios
    .get("http://localhost:8000/products")
    .then((res) => res.data)
    .catch((err) => console.log(err));
  return data;
}

export default async function HomePage() {
  const data = await getData();
  return (
    <div className="flex flex-col p-5">
      <div className="flex mb-5 justify-between gap-1.5">
        <div className="flex gap-1 min">
          <Input placeholder="Title" />
          <Input placeholder="Artist" />
          <Input placeholder="Year" />
          <Input placeholder="Seller" />
          <Input placeholder="Copies" />
        </div>
        <div className="flex w-full gap-1.5">
          <Button className="bg-blue-600 hover:bg-blue-500 w-28">Add</Button>
          {/* <Button className="bg-green-700 hover:bg-green-600">Edit</Button>
        <Button variant="destructive">Delete</Button> */}
        </div>
      </div>
      <div className="w-full max-w-3xl">
        <DataTable columns={columns} data={data} />
      </div>
    </div>
  );
}
