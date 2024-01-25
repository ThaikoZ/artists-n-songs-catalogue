"use client";

import { ColumnDef } from "@tanstack/react-table";
import { MoreHorizontal } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

export type Song = {
  song_id: number;
  title: string;
  album_title: string;
  duration_in_seconds: number;
  sold_copies: number;
};

export const columns: ColumnDef<Song>[] = [
  {
    accessorKey: "title",
    header: "Title",
  },

  {
    accessorKey: "album_title",
    header: "Album Title",
  },
  {
    accessorKey: "duration_in_seconds",
    header: "Duration (s)",
  },
  {
    accessorKey: "author",
    header: "Author",
  },
  {
    accessorKey: "sold_copies",
    header: "Sold Copies",
  },
  {
    id: "actions",
    cell: ({ row }) => {
      const song = row.original;

      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="h-8 w-8 p-0">
              <span className="sr-only">Open menu</span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuLabel>Options</DropdownMenuLabel>
            <DropdownMenuItem
              onClick={() => console.log("Show details of " + song.title)}
            >
              Show details
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>Edit</DropdownMenuItem>
            <DropdownMenuItem>Delete</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  },
];
