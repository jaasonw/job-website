"use client";

import { Navbar } from "flowbite-react";

export default function Nav() {
  return (
    <nav className="flex w-full items-center justify-center border shadow-sm">
      <Navbar fluid rounded className="max-w-screen-xl w-full px-6">
        <Navbar.Brand href="/">
          <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">
            SWEify
          </span>
        </Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className=" font-medium">
          <Navbar.Link
            href="#"
            className="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
          >
            About
          </Navbar.Link>
          <Navbar.Link
            href="https://github.com/jaasonw/sweify/issues"
            className="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
          >
            Report a Bug
          </Navbar.Link>
          <Navbar.Link
            href="#"
            className="block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
          >
            Contact
          </Navbar.Link>
        </Navbar.Collapse>
      </Navbar>
    </nav>
  );
}
