import { motion as m } from "framer-motion";


const Sumaraze = () => {
    return (
        <m.div initial={{ y: "100%" }} animate={{ y: "0%" }} transition={{ duration: 0.75, ease: "easeOut" }}
            exit={{ opacity: 1 }}
        >
            <div>
                <h1>Sumaraze page</h1>
            </div>
        </m.div>
    );
}

export default Sumaraze;