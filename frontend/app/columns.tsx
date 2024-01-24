"use client";

import { ColumnDef } from "@tanstack/react-table";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Product = {
  id: number;
  album: string;
  artist: string;
  year: number;
  seller: string;
  copies: number;
};

export const columns: ColumnDef<Product>[] = [
  {
    accessorKey: "album",
    header: "Album",
  },
  {
    accessorKey: "artist",
    header: "Artist",
  },
  {
    accessorKey: "year",
    header: "Year",
  },
  {
    accessorKey: "seller",
    header: "Seller",
  },
  {
    accessorKey: "copies",
    header: "Copies",
  },
];
