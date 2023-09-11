"use client";

import { useParams } from "next/navigation";

const UserProfile = () => {
  const { id } = useParams();
  return (
    <>Name = {id}</>
  );
};

export default UserProfile;