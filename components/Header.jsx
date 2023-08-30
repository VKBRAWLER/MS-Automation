"use client"
import { useState, useEffect } from 'react';
import Link from 'next/link';
import { HiMenu, HiX } from 'react-icons/hi';

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const [isLaptopScreen, setIsLaptopScreen] = useState(true);

  // Function to handle window resize
  const handleResize = () => {
    if (window.innerWidth >= 768) {
      setIsLaptopScreen(true);
    } else {
      setIsLaptopScreen(false);
    }
  };

  // Add event listener for window resize
  useEffect(() => {
    handleResize(); // Initial check
    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <nav className="bg-gradient-to-r from-blue-400 to-purple-500 p-4 flex items-center justify-between relative">
      {!isLaptopScreen && (
          <div>
          <button
            onClick={toggleMenu}
            className="text-white p-2 focus:outline-none"
          >
            {menuOpen ? <HiX size={24} /> : <HiMenu size={24} />}
          </button>
        </div>
      )}
      {/* Logo */}
      <div className="flex items-center">
        <div className="h-10 w-10 rounded-full bg-white flex items-center justify-center">
          {/* You can place your logo image here */}
          <span className="text-blue-500 text-xl font-semibold">Logo</span>
        </div>
      </div>

      {/* Middle: Navigation Links (Hidden on Mobile) */}
      {isLaptopScreen && (
        <ul className="md:flex space-x-14  ">
          <li>
            <Link href="/">
              <p className="text-white hover:text-blue-300 cursor-pointer">
                Home
              </p>
            </Link>
          </li>
          <li>
            <Link href="/all-threats">
              <p className="text-white hover:text-blue-300 cursor-pointer">
                All Threats
              </p>
            </Link>
          </li>
          <li>
            <Link href="/about-us">
              <p className="text-white hover:text-blue-300 cursor-pointer">
                About Us
              </p>
            </Link>
          </li>
          <li>
            <Link href="/help-center">
              <p className="text-white hover:text-blue-300 cursor-pointer">
                Help Center
              </p>
            </Link>
          </li>
        </ul>
      )}

      {/* Dropdown Menu (Absolute Position) */}
      {menuOpen && !isLaptopScreen && (
        <div className="absolute top-full left-2 mt-2 bg-white text-black border rounded-lg shadow-lg">
          <ul className="py-2 px-4 space-y-2">
            <li>
              <Link href="/">
                <p className="hover:text-blue-300 cursor-pointer">
                  Home
                  </p>
              </Link>
            </li>
            <li>
              <Link href="/all-threats">
                <p className="hover:text-blue-300 cursor-pointer">
                  All Threats
                </p>
              </Link>
            </li>
            <li>
              <Link href="/about-us">
                <p className="hover:text-blue-300 cursor-pointer">About Us</p>
              </Link>
            </li>
            <li>
              <Link href="/help-center">
                <p className="hover:text-blue-300 cursor-pointer">
                  Help Center
                </p>
              </Link>
            </li>
          </ul>
        </div>
      )}

      {/* Right side: Sign Up Box with Border */}
      <div className="border-2 border-white rounded-lg px-4 py-2">
        <button className="text-white">Sign Up</button>
      </div>
    </nav>
  );
};

export default Header;
