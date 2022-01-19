dataframe.loc[
    (
            (
                    (
                            (dataframe['ema12'] > dataframe['ema26']) &  #
                            (dataframe['ema12'].shift(1) < dataframe['ema26'].shift(
                                1)) &  # EMA12 is currently crossing above the EMA26
                            (dataframe['macd'] > dataframe['macdSignal'])  # MACD is above the Signal
                    )
                    |  # OR
                    (
                            (dataframe['ema12'] > dataframe['ema26']) &  #
                            (dataframe['macd'] > dataframe['macdSignal']) &
                            (dataframe['macd'].shift(1) < dataframe['macdSignal'].shift(1))
                    # MACD is currently crossing above the Signal
                    )
            )
            &  # AND
            (self.watchdog.buy_indicator &
             (dataframe['sma50'] > dataframe['sma200']) &
             (dataframe['volume'] > 0) &  # Make sure Volume

             )

    ),
    'buy'] = 1
return dataframe