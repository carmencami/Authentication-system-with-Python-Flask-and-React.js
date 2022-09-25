import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Private = () => {
  const { store, actions } = useContext(Context);
  const navigate = useNavigate();

  return store.token ? (
    <div className="text-center mt-5">
      <h1>Área privada</h1>
    </div>
  ) : (
    navigate("/login")
  );
};
