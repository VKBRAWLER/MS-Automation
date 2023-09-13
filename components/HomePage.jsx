import Head from 'next/head';
import Image from 'next/image';
import React from 'react'

const HomePage = () => {
    const w = 400;
  return (
    <>
      <Head>
        <title>Welcome to Surveysnap</title>
        <meta name="description" content="Welcome to Surveysnap - Your survey platform" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="w-full bg-colo">
      <div className="bg-gradient-to-r from-blue-400 to-purple-500 text-white p-6 text-center">
        <h1 className="text-4xl font-semibold">Welcome to Surveysnap</h1>
        <p className="mt-4 text-xl">Your Survey Platform</p>
      </div>
        <section className="text-center flex justify-between gap-20 flex-wrap md:flex-nowrap m-5">
            <div className="w-full my-auto">
              <h2 className="text-2xl font-semibold mb-4">About Surveysnap</h2>
              <p className="text-gray-700 px-10">
              Surveysnap is a modern and easy-to-use survey platform that helps you collect valuable feedback from your audience. Our platform provides powerful analytics and reporting tools, making it easy to gain insights from your survey data.
              </p>
            </div>
            <Image
              src="/img/DisplayImages/Image01.png"
              alt="Survey Image"
              className="mx-auto"
              width={w}
              height={w}
            />
        </section>
        <section className="text-center flex justify-between gap-20 flex-wrap flex-row-reverse md:flex-nowrap m-5">
            <div className="w-full my-auto">
              <h2 className="text-2xl font-semibold mb-4">Get Started Today</h2>
              <p className="text-gray-700 px-10">
              Join thousands of businesses and organizations who trust Surveysnap to gather feedback, make data-driven decisions, and improve their products and services.
              </p>
            </div>
            <Image
              src="/img/DisplayImages/Image02.png"
              alt="Survey Image"
              className="mx-auto"
              width={w}
              height={w}
            />
        </section>
      </main>
    </>
  )
}

export default HomePage