import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "./Navbar";
import { ThemeProvider } from "@/app/providers/ThemeProvider";
import Container from "./components/Container";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-[#f5f4f7] dark:bg-[#0a0b08]`}>
        <Navbar />
        <Container>{children}</Container>
      </body>
    </html>
  );
}
