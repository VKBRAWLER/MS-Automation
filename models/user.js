import { Schema, model, models } from "mongoose";
// models is the collection of all the model that is associated with the mongoose library
const UserSchema = new Schema({
    email: {
        type : String,
        unique : [true, 'email already in use'],
        required : [true, 'email already in use']
    },
    username: {
        type: String,
        required : [true, 'username is required'],
        match: [/^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$/, "Username invalid, it should contain 8-20 alphanumeric letters and be unique!"],
        image: {
            type: String,
        }    
    }
});

const User = models.User || model("User", UserSchema);
// if a "User" already exists, models assign the existing one to avoid redefining model and ensuring the existing one be used.
// Otherwise it will create a new one.
export default User;