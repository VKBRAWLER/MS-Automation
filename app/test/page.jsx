"use client";
import React, { useState, useRef } from 'react';
import { AiFillDelete } from "react-icons/ai";
import { FcAddImage } from "react-icons/fc";
import Image from 'next/image';
const image = () => {
  const [image, setImage] = useState(null);
  const getImage = (e) => {
    const img_file = e.target.files[0];
    console.log(img_file);
      setImage(img_file);
  }
  const saveImg = () => {
    alert("Save hoja sim sim");
  }
  return (
    <>
    Image Test
    <section className="flex flex-wrap h-auto w-full m-5 p-4 bg-cyan-200 rounded-3xl">
       <div className='flex justify-between mb-5 w-full'>
          <div>Order: <input type="number" className='w-8 bg-cyan-100'/></div>
          <div><span>Type: </span><select name="cars" id="cars">
            <option value="single">Single Q/A</option>
            <option value="mcq">MCQ</option>
          </select>
          </div>
          <div><AiFillDelete className='w-6 h-6'/></div>
       </div>
        <div className='w-full'>
        <span>Q1. </span><textarea name="" id="ito" className='w-[calc(100%-30px)] p-2 resize-none bg-cyan-100'/>
        </div>
        <div className='m-5'>
          <span>Options</span>
          <ol className='list-decimal'>
            <li><input type="text" className='m-2 bg-cyan-100'/>
            <div className='image-input inline'>
                <input type='file' className='sr-only' onChange={getImage} />
              <FcAddImage className='inline w-8 h-8 cursor-pointer' 
              onClick={(e)=>{console.log(e.target.parentNode.parentNode.firstChild.click())}}/>
            </div>
            <div className="img-box relative">
            {image? <img src={URL.createObjectURL(image)} className='img-view' />: <img src="img/Raw Images/Image01.png" className='img-view'/> }
            {image? 
              <><button className="absolute top-0 right-0 w-12 h-5 ">delete</button>
                <div className="absolute bottom-0 w-full h-10 bg-blue-200 flex">
                <button className="w-1/3 h-full bg-slate-50"><span>Sqaure</span></button>
                <button className="w-1/3 h-full bg-slate-50 border-x-2 border-black"><span>Cover</span></button>
                <button className="w-1/3 h-full bg-slate-50"><span>Change Image</span></button>
              </div></>
            :<></>
            }
            </div>
            </li>
          </ol>
        </div>
      </section>
        <button className='bg-blue-500 p-4 rounded-2xl' onClick={saveImg}>save</button>

    </>
  )
}

export default image