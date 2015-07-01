#ifndef VRRWRITER_HPP
#define VRRWRITER_HPP

#include <iostream>
#include <utility>

#include "generator/Classes.hpp"


class VRR_Algorithm_Base;

class VRR_Writer
{   
    public:
        VRR_Writer(const VRR_Algorithm_Base & vrr_algo_);

        void WriteVRR(std::ostream & os) const;

        void WriteIncludes(std::ostream & os) const;
        void AddConstants(std::ostream & os) const;
        void DeclarePrimArrays(std::ostream & os) const;
        void DeclarePrimPointers(std::ostream & os) const;

        void WriteVRRFile(std::ostream & os) const;
        void WriteVRRHeaderFile(std::ostream & os) const;

    private:
        VRRMap vrrmap_;
        GaussianMap vrramreq_;

        void WriteVRRInline_(std::ostream & os) const;
        void WriteVRRExternal_(std::ostream & os) const;

        void WriteAccumulate_(std::ostream & os, int am) const;

        void WriteVRRSteps_(std::ostream & os) const;
        void WriteVRRSteps_(std::ostream & os, const GaussianSet & greq, const std::string & num_n) const;
};

#endif
