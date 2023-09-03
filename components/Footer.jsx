import Link from 'next/link';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-8">
      <div className="mx-auto flex flex-wrap justify-evenly text-center">
        {/* Redirect Links Section */}
        <div className="w-full md:w-1/2 lg:w-1/4 mb-6 md:mb-0">
          <h3 className="text-2xl font-semibold mb-4">Redirect Links</h3>
          <ul className="space-y-2">
            <li>
              <Link href="/about">About Us</Link>
            </li>
            <li>
              <Link href="/services">Services</Link>
            </li>
            <li>
              <Link href="/blog">Blog</Link>
            </li>
            <li>
              <Link href="/contact">Contact</Link>
            </li>
          </ul>
        </div>

        {/* Developer Contact Section */}
        <div className="w-full md:w-1/2 lg:w-1/4 mb-6 md:mb-0">
          <h3 className="text-2xl font-semibold mb-4">Developer Contact</h3>
          <p>
            Have questions or need support?<br />
            Contact our developer:
          </p>
          <a href="mailto:developer@example.com" className="mt-2 text-blue-300 hover:underline">
            developer@example.com
          </a>
        </div>

        {/* Credentials Section */}
        <div className="w-full md:w-1/2 lg:w-1/4">
          <h3 className="text-2xl font-semibold mb-4">Credentials</h3>
          <p>
            Surveysnap &copy; 2023<br />
            All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
