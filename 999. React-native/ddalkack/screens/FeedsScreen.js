import React, { useContext } from "react";
import { StyleSheet, View } from "react-native";
import FloatingWriteButton from "../components/FloatingWriteButton";
import LogContext from "../contexts/LogContext";
import FeedList from "../components/FeedList";

function FeedsScreen() {
  const { logs } = useContext(LogContext);
  return (
    <View style={stlyes.block}>
      <FeedList logs={logs} />
      <FloatingWriteButton />
    </View>
  );
}

const stlyes = StyleSheet.create({
  block: {
    flex: 1,
  },
});

export default FeedsScreen;
