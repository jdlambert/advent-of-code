(ns main (:require [clojure.string :as str]))

(defmulti exec (fn [_ [op]] op))

(defmethod exec :inc [state [_ register]]
  (-> state (update register inc) (update :pc inc)))

(defmethod exec :tpl [state [_ register]]
  (-> state (update register * 3) (update :pc inc)))

(defmethod exec :hlf [state [_ register]]
  (-> state (update register quot 2) (update :pc inc)))

(defmethod exec :jmp [state [_ offset]]
  (update state :pc + offset))

(defmethod exec :jie [state [_ register offset]]
  (update state :pc + (if (even? (state register)) offset 1)))

(defmethod exec :jio [state [_ register offset]]
  (update state :pc + (if (= 1 (state register)) offset 1)))

(defn parse-arg [arg]
  (if (re-find #"\d+" arg)
    (parse-long arg)
    (keyword arg)))

(defn parse-line [line]
  (let [[op & args] (str/split line #"[ ,]+")]
    (into [(keyword op)] (map parse-arg args))))

(def program
  (->> (slurp "input.txt")
       str/split-lines
       (mapv parse-line)))

(defn run [state]
  (->> state
       (iterate #(exec % (program (:pc %))))
       (drop-while #(< -1 (:pc %) (count program)))
       first
       :b))

(println (run {:a 0 :b 0 :pc 0}))
(println (run {:a 1 :b 0 :pc 0}))