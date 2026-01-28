class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda b: b[1], reverse=True)

        units = 0
        for boxes, units_per_box in boxTypes:
            take = min(truckSize, boxes)
            units += take * units_per_box
            truckSize -= take
            if truckSize == 0:
                break

        return units