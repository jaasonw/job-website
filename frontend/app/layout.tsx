import Nav from "$lib/components/Navbar";
import "./globals.css";
import { Inter } from "next/font/google";
export const metadata = {
  title: "title",
  description: "description",
};

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-inter",
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} font-sans`}>
      <body>
        <Nav />
        <main className="flex flex-col w-full justify-center items-center">
          {children}
        </main>
        <footer className="flex flex-col text-xs w-full p-4 items-center text-center text-white bg-black">
          <span>
            Disclaimer: All the jobs displayed on this website are collected
            from different public sources. We don&apos;t have any partnership or
            gain with the companies.
          </span>
          <span>
            If I helped your job search in any way,{" "}
            <a href="https://jason-wong.me/donate" className="underline">
              consider funding my boba addiction
            </a>
          </span>
          <span>
            © 2023 | Made by{" "}
            <a href="https://jason-wong.me/" className="underline">
              Jason Wong
            </a>{" "}
            | Open source under{" "}
            <a href="https://github.com/jaasonw/sweify" className="underline">
              MIT
            </a>{" "}
            | Inspired by{" "}
            <a href="https://www.freshswe.com/" className="underline">
              freshSWE
            </a>
          </span>
        </footer>
      </body>
    </html>
  );
}
