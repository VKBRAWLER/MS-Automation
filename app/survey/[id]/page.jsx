"use client";
import React, { useEffect } from 'react';
import { AiFillDelete } from "react-icons/ai";
import { FcAddImage } from "react-icons/fc";
import Image from 'next/image';
const Survey = ({ params }) => {
  const textareaResize = () => {
    document.querySelectorAll('textarea').forEach( element => {
      element.style.height = `${element.scrollHeight}px`;
      element.addEventListener('input', event => {
        event.target.style.height = 'auto'; 
        event.target.style.height = `${event.target.scrollHeight}px`;
        console.log(event.target.style.height);
        })
    });
  } 
    useEffect(() => {
      textareaResize();
    }, [])
    
  return (
    <>
    <h1>Create new Survey</h1>
    <div className="flex flex-wrap w-full">
      <section className="flex flex-wrap h-auto w-full m-5 p-4 bg-cyan-200 rounded-3xl">
       <div className='flex justify-between mb-5 w-full'>
          <div>Order: <input type="number" className='w-8 bg-cyan-100'/></div>
          <div><span>Type: </span><select name="cars" id="cars">
            <option value="single">Single Q/A</option>
            <option value="mcq">MCQ</option>
          </select>
          </div>
          <div><AiFillDelete/></div>
       </div>
        <div className='w-full'>
        <span>Q1. </span><textarea name="" id="ito" className='w-[calc(100%-30px)] p-2 resize-none bg-cyan-100'/>
        </div>
        <div className='m-5'>
          <span>Options</span>
          <ol className='list-decimal'>
            <li><input type="text" className='m-2 bg-cyan-100'/><FcAddImage className='inline'/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><FcAddImage className='inline'/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><FcAddImage className='inline'/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><FcAddImage className='inline'/></li>
          </ol>
        </div>
      </section>
      <section className="flex flex-wrap h-auto w-full m-5 p-4 bg-cyan-200 rounded-3xl">
       <div className='flex justify-between mb-5 w-full'>
          <div>Order: <input type="number" className='w-8 bg-cyan-100'/></div>
          <div><span>Type: </span><select name="cars" id="cars">
            <option value="single">Single Q/A</option>
            <option value="mcq">MCQ</option>
          </select>
          </div>
          <div><AiFillDelete/></div>
       </div>
        <div className='w-full'>
        <span>Q1. </span><textarea name="" id="ito" className='w-[calc(100%-30px)] p-2 resize-none bg-cyan-100'/>
        </div>
        <div className='m-5'>
          <span>Options</span>
          <ol className='list-decimal'>
            <li><input type="text" className='m-2 bg-cyan-100'/><Image src={"/img/DisplayImages/Image01.png"} height={200} width={200}/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><Image src={"/img/DisplayImages/Image01.png"} height={200} width={200}/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><Image src={"/img/DisplayImages/Image01.png"} height={200} width={200}/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><Image src={"/img/DisplayImages/Image01.png"} height={200} width={200}/></li>
          </ol>
        </div>
      </section>
      <section className="flex flex-wrap h-auto w-full m-5 p-4 bg-cyan-200 rounded-3xl">
       <div className='flex justify-between mb-5 w-full'>
          <div>Order: <input type="number" className='w-8 bg-cyan-100'/></div>
          <div><span>Type: </span><select name="cars" id="cars">
            <option value="single">Single Q/A</option>
            <option value="mcq">MCQ</option>
          </select>
          </div>
          <div><AiFillDelete/></div>
       </div>
        <div className='w-full'>
        <span>Q1. </span><textarea name="" id="ito" className='w-[calc(100%-30px)] p-2 resize-none bg-cyan-100'/>
        </div>
        <div className='m-5'>
          <span>Options</span>
          <ol className='list-decimal'>
            <li><input type="text" className='m-2 bg-cyan-100'/><input type='file'/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><input type='file'/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><input type='file'/></li>
            <li><input type="text" className='m-2 bg-cyan-100'/><input type='file'/></li>
          </ol>
        </div>
      </section>
    </div>
    </>
  )
}
export default Survey